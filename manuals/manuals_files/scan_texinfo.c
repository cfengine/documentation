/*****************************************************************************/
/*                                                                           */
/* File: chew.c                                                              */
/*                                                                           */
/* Created: Sat Jan 26 20:12:14 2008                                         */
/*                                                                           */
/* Author:                                                                   */
/*                                                                           */
/* Revision: $Id$                                                            */
/*                                                                           */
/* Description:                                                              */
/*                                                                           */
/*****************************************************************************/

#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

#define CF_SCALAR 's'

#define false 0
#define true  1
#define CF_BUFSIZE 2048
#define cf_error 1

/*************************************************************************/
/* Ontology                                                              */
/*************************************************************************/

struct Topic
   {
   char *topic_type;
   char *topic_name;
   char *comment;
   struct Occurrence *occurrences;
   struct TopicAssociation *associations;
   struct Topic *next;
   };

struct TopicAssociation
   {
   char *assoc_type;
   char *fwd_name;
   char *bwd_name;
   struct Rlist *associates;
   char *associate_topic_type;
   struct TopicAssociation *next;
   };

/*******************************************************************/


struct Rlist
   {
   void *item;
   char type;
   struct Rlist *state_ptr; /* Points to "current" state/element of sub-list */
   struct Rlist *next;
   };


struct Item
   {
   char  *name;
   struct Item *next;
   };

/*****************************************************************************/

void Manual(char *prefix,char *str,char *file);
void ProcessFile(char *file,FILE *fin,char *context,char *prefix);
char *CanonifyName(char *str);
void AddTopic(struct Topic **list,char *name,char *type,int nr);
int TopicExists(struct Topic *list,char *topic_name,char *topic_type);
void AppendItem (struct Item **liststart,char *itemstring);
char ToLower (char ch);
char ToUpper (char ch);
char *ToUpperStr (char *str);
char *ToLowerStr (char *str);
char *GetTitle(char *base, char *type);
char *GetTopicType(struct Topic *list,char *topic_name);
void AddTopicAssociation(struct TopicAssociation **list,char *fwd_name,char *bwd_name,char *topic_type,char *associate,int verify);
struct Topic *GetTopic(struct Topic *list,char *topic_name);
struct TopicAssociation *AssociationExists(struct TopicAssociation *list,char *fwd,char *bwd,int verify);
struct Rlist *IdempPrependRScalar(struct Rlist **start,void *item, char type);
struct Rlist *KeyInRlist(struct Rlist *list,char *key);
struct Rlist *PrependRlist(struct Rlist **start,void *item, char type);

/*****************************************************************************/

main(int argc, char **argv)

{
// Prefix for Web pages:  http://cfengine.com/inside/manuals/
// Prefix for Nova, etc: /

if (argv[3] && strcmp(argv[3],"web") == 0)
   {
   Manual(argv[1],argv[2],"/docs/");
   }
else
   {
   Manual(argv[1],argv[2],"/docs/");
   }
}

/*****************************************************************************/

void Manual(char *context,char *file,char *prefix)

{ FILE *fin;
  char name[2048];

/* Start with the main doc file */
 
if ((fin = fopen(file,"r")) == NULL)
   {
   printf("File missing\n");
   exit(0);
   }

strcpy(name,file);
*(strchr(name,'.')) = '\0'; // strip extension

ProcessFile(name,fin,context,prefix);

fclose(fin);
}

/*****************************************************************************/

void ProcessFile(char *document,FILE *fin,char *context,char *prefix)

{ char tmp[2048],line[2048],type[2048],url[2048],title[2048],*sp;
  char chapter[2048],section[2048],subsection[2048],script[2048];
  struct Topic *tp,*topics = NULL;
  struct Item *ip,*scriptlog = NULL;
  int lineno = 0;  

strcpy(chapter,"Special Topics Guide");
strcpy(section,"Special Topics Guide");

while (!feof(fin))
   {
   fgets(line,2047,fin);
   lineno++;

   if (sp = strstr(line,"<dt>&lsquo;<samp><code>"))
      {
      sscanf(sp+strlen("<dt>&lsquo;<samp><code>"),"%[^<]",title);
      sprintf(script,"%s::\n",CanonifyName(title));
      AppendItem(&scriptlog,script);
      sprintf(script," \"%s%s.html#%s\"\n",prefix,document,url);
      AppendItem(&scriptlog,script);
      sprintf(script,"  represents => { \"document\" };\n");
      AppendItem(&scriptlog,script);

      AddTopic(&topics,title,"documentation",lineno);

      if (tp = GetTopic(topics,title))
         {
         AddTopicAssociation(&(tp->associations),"is contained in","contains","files",document,true);
         }

      }

   if (sp = strstr(line,"<a name=\""))
      {
      memset(url,0,2048);
      sscanf(sp+strlen("<a name=\""),"%[^\"]",url);
      }

   if (sp = strstr(line,"<title>"))
      {
      memset(url,0,2048);
      sscanf(sp+strlen("<title>"),"%[^<]",title);
      
      if (strncmp(document,"st-",3) == 0)
         {
         sprintf(script,"special_topics_guides::\n");
         AppendItem(&scriptlog,script);
         sprintf(script," \"%s%s.html\"\n",prefix,document);
         AppendItem(&scriptlog,script);
         sprintf(script,"  represents => { \"%s\" };\n",title);
         AppendItem(&scriptlog,script);
         }
      else
         {
         sprintf(script,"manuals::\n");
         AppendItem(&scriptlog,script);
         sprintf(script," \"%s%s.html\"\n",prefix,document);
         AppendItem(&scriptlog,script);
         sprintf(script,"  represents => { \"%s\" };\n",title);
         AppendItem(&scriptlog,script);
         }
      }

   if (sp = strstr(line,"class=\""))       
      {
      memset(type,0,2048);
      sscanf(sp+strlen("class=\""),"%[^\"]",type);

      if (strstr(type,"unnumbered"))
         {
         strcpy(title,GetTitle(sp,type));
         
         sprintf(script,"%s::\n",CanonifyName(title));
         AppendItem(&scriptlog,script);
         sprintf(script," \"%s%s.html#%s\"\n",prefix,document,url);
         AppendItem(&scriptlog,script);
         sprintf(script,"  represents => { \"Text section\" };\n");
         AppendItem(&scriptlog,script);
         strcpy(subsection,title);

         
         AddTopic(&topics,title,section,lineno);

         if (strcmp(section,"Special Topics Guide") == 0)
            {
            strcpy(section,title);
            }
         
         if (tp = GetTopic(topics,section))
            {
            AddTopicAssociation(&(tp->associations),"discussed in","discusses","short topic",section,true);
            }
         }

      
      if (strstr(type,"subsection"))
         {
         strcpy(title,GetTitle(sp,type));
         
         sprintf(script,"%s::\n",CanonifyName(title));
         AppendItem(&scriptlog,script);
         sprintf(script," \"%s%s.html#%s\"\n",prefix,document,url);
         AppendItem(&scriptlog,script);
         sprintf(script,"  represents => { \"manual %s\" };\n",type);
         AppendItem(&scriptlog,script);
         strcpy(subsection,title);
         
         AddTopic(&topics,subsection,section,lineno);
         continue;

         if ((tp = GetTopic(topics,subsection)) && (strlen(section) > 0))
            {
            AddTopicAssociation(&(tp->associations),"is a subsection of","has subsection","manual",section,true);
            }
         }

      if (strstr(type,"section"))
         {
         strcpy(title,GetTitle(sp,type));
         sprintf(script,"%s::\n",CanonifyName(title));
         AppendItem(&scriptlog,script);
         sprintf(script," \"%s%s.html#%s\"\n",prefix,document,url);
         AppendItem(&scriptlog,script);
         sprintf(script,"  represents => { \"manual section %s\" };\n",title);
         AppendItem(&scriptlog,script);

         script[0] = '\0';
         strcpy(section,title);
         strcpy(subsection,"");
         AddTopic(&topics,section,chapter,lineno);

         if (tp = GetTopic(topics,subsection))
            {
            AddTopicAssociation(&(tp->associations),"discussed in","discusses","manual",chapter,true);
            }
         continue;
         }

      if (strstr(type,"chapter"))
         {
         strcpy(title,GetTitle(sp,type));
         sprintf(script,"%s::\n",CanonifyName(title));
         AppendItem(&scriptlog,script);
         sprintf(script," \"%s%s.html#%s\"\n",prefix,document,url);
         AppendItem(&scriptlog,script);
         
         sprintf(script,"  represents => { \"manual chapter\" };\n");
         AppendItem(&scriptlog,script);
         
         strcpy(chapter,title);
         strcpy(section,"");
         strcpy(subsection,"");
         AddTopic(&topics,chapter,title,lineno);

         if (tp = GetTopic(topics,subsection))
            {
            AddTopicAssociation(&(tp->associations),"discussed in","discusses","Documentation",section,true);
            }

         continue;
         }

      if (strstr(type,"smallexample"))
         {
         // Find the nearest section name for topic name
         
         memset(title,0,2048);
         
         if (strlen(subsection) != 0)
            {
            strcpy(title,subsection);
            }
         else if (strlen(section) != 0)
            {
            strcpy(title,section);
            }
         else
            {
            strcpy(title,chapter);
            }

         sprintf(script,"%s::\n",CanonifyName(title));
         AppendItem(&scriptlog,script);
         sprintf(script," \"%s%s.html#%s\"\n",prefix,document,url);
         AppendItem(&scriptlog,script);

         sprintf(script,"  represents => { \"code example\" };\n");
         AppendItem(&scriptlog,script);
         continue;
         }

      }   
   }

printf("\nbundle knowledge %s\n\n{\n",CanonifyName(document));

printf("topics:\n\n");

printf("\"%s\";\n",document);

for (tp = topics; tp != NULL; tp=tp->next)
   {
   if (strlen(tp->topic_type) > 0)
      {
      printf("%s::\n",CanonifyName(tp->topic_type));
      }

   printf("    \"%s\" ",tp->topic_name);

   if (tp->associations)
      {
      struct TopicAssociation *ta = tp->associations;
      struct Rlist *list = ta->associates;
      
      printf(" association => a(\"%s\",\"%s\",\"%s\")",
             ta->fwd_name,
             list->item,
             ta->bwd_name);
      }
   
   printf(";\n");
   }

printf("\n\noccurrences:\n\n");

for (ip = scriptlog; ip != NULL; ip=ip->next)
   {
   printf("%s",ip->name);
   }


printf("}\n\n");
}

/******************************************************************/

char *GetTitle(char *base,char *type)

{ static char tmp[CF_BUFSIZE];
  char buffer[CF_BUFSIZE];
  char *sp,*to;
  
tmp[0] = '\0';
memset(tmp,0,CF_BUFSIZE);

if (strstr(type,"unnumbered"))
   {
   sscanf(base+strlen("class=\"xx")+strlen(type),"%[^(\n]",buffer);
   }
else
   {
   sscanf(base+strlen("class=\"xx")+strlen(type),"%*s %[^(\n]",buffer);
   }

for (sp = buffer,to = tmp; *sp != '\0'; sp++)
   {
   switch (*sp)
      {
      case '<':
          
          while (*++sp != '>')
             {
             if (*sp == '\0')
                {
                *to = '\0';
                sp--;
                continue;
                }
             }
          break;

      case '&':

          if (*(sp-1) != '\\')
             {
             while (*++sp != ';')
                {
                if (*sp == '\0')
                   {
                   *to = '\0';
                   sp--;
                   continue;
                   }
                }
             }

          break;
          
      case '\'':
      case '`':
          break;
          
      default:
          *to++ = *sp;
          break;
      }
   }

if (sp = strstr(tmp," (body template)"))
   {
   *sp = '\0';
   }

sp = tmp + strlen(tmp)-1;

if (isspace(*sp))
   {
   *sp = '\0';
   }

return tmp;
}

/*****************************************************************************/

char *CanonifyName(char *str)

{ static char buffer[2048];
  char *sp;

memset(buffer,0,2048);
strcpy(buffer,str);

for (sp = buffer; *sp != '\0'; sp++)
    {
    switch (*sp)
       {
       default:
           if (!isalnum((int)*sp))
              {
              *sp = '_';
              }
           
       }    
    }

return buffer;
}

/*****************************************************************************/

void AddTopic(struct Topic **list,char *name,char *type,int nr)

{ struct Topic *tp;

if (TopicExists(*list,name,type))
   {
//   fprintf(stderr,"Topic %s already defined at line %d\n",name,nr);
   return;
   }
 
if ((tp = (struct Topic *)malloc(sizeof(struct Topic))) == NULL)
   {
   printf("Memory failure in AddTopic");
   exit(1);
   }

if ((tp->topic_name = strdup(name)) == NULL)
   {
   printf("Memory failure in AddTopic");
   exit(1);
   }

if ((tp->topic_type = strdup(type)) == NULL)
   {
   printf("Memory failure in AddTopic");
   exit(1);
   }

tp->comment = NULL;
tp->associations = NULL;
tp->occurrences = NULL;
tp->next = *list;
*list = tp;
}


/*****************************************************************************/
/* Level                                                                     */
/*****************************************************************************/

int TopicExists(struct Topic *list,char *topic_name,char *topic_type)

{ struct Topic *tp;

for (tp = list; tp != NULL; tp=tp->next)
   {
   if (strcmp(tp->topic_name,topic_name) == 0)
      {
      if (topic_type && strcmp(tp->topic_type,topic_type) != 0)
         {
         //fprintf(stderr,"Scan: Topic \"%s\" exists, but its type \"%s\" does not match promised type \"%s\"\n",topic_name,tp->topic_type,topic_type);
         }
      return true;
      }
   }

return false;
}


/*****************************************************************************/

struct Topic *GetTopic(struct Topic *list,char *topic_name)

{ struct Topic *tp;

for (tp = list; tp != NULL; tp=tp->next)
   {
   if (strcmp(topic_name,tp->topic_name) == 0)
      {
      return tp;          
      }
   }

return NULL;
}

/*****************************************************************************/

struct Topic *GetCanonizedTopic(struct Topic *list,char *topic_name)

{ struct Topic *tp;

for (tp = list; tp != NULL; tp=tp->next)
   {
   if (strcmp(topic_name,CanonifyName(tp->topic_name)) == 0)
      {
      return tp;          
      }
   }

return NULL;
}

/*****************************************************************************/

char *GetTopicType(struct Topic *list,char *topic_name)

{ struct Topic *tp;

for (tp = list; tp != NULL; tp=tp->next)
   {
   if (strcmp(topic_name,tp->topic_name) == 0)
      {
      return tp->topic_type;
      }
   }

return NULL;
}


/*********************************************************************/

void AppendItem (struct Item **liststart,char *itemstring)

{ struct Item *ip, *lp;
  char *sp,*spe = NULL;

if ((ip = (struct Item *)malloc(sizeof(struct Item))) == NULL)
   {
   perror("malloc");
   exit(1);
   }

if (*liststart == NULL)
   {
   *liststart = ip;
   }
else
   {
   for (lp = *liststart; lp->next != NULL; lp=lp->next)
      {
      }

   lp->next = ip;
   }

ip->name = strdup(itemstring);
ip->next = NULL;
}


/*********************************************************************/
/* TOOLKIT : String                                                  */
/*********************************************************************/

char ToLower (char ch)

{
if (isdigit((int)ch) || ispunct((int)ch))
   {
   return(ch);
   }

if (islower((int)ch))
   {
   return(ch);
   }
else
   {
   return(ch - 'A' + 'a');
   }
}


/*********************************************************************/

char ToUpper (char ch)

{
if (isdigit((int)ch) || ispunct((int)ch))
   {
   return(ch);
   }

if (isupper((int)ch))
   {
   return(ch);
   }
else
   {
   return(ch - 'a' + 'A');
   }
}

/*********************************************************************/

char *ToUpperStr (char *str)

{ static char buffer[CF_BUFSIZE];
  int i;

memset(buffer,0,CF_BUFSIZE);
  
if (strlen(str) >= CF_BUFSIZE)
   {
   char *tmp;
   tmp = malloc(40+strlen(str));
   exit(1);
   }

for (i = 0;  (str[i] != '\0') && (i < CF_BUFSIZE-1); i++)
   {
   buffer[i] = ToUpper(str[i]);
   }

buffer[i] = '\0';

return buffer;
}


/*********************************************************************/

char *ToLowerStr (char *str)

{ static char buffer[CF_BUFSIZE];
  int i;

memset(buffer,0,CF_BUFSIZE);

if (strlen(str) >= CF_BUFSIZE-1)
   {
   char *tmp;
   tmp = malloc(40+strlen(str));
   printf("String too long in ToLowerStr: %s",str);
   exit(1);
   }

for (i = 0; (str[i] != '\0') && (i < CF_BUFSIZE-1); i++)
   {
   buffer[i] = ToLower(str[i]);
   }

buffer[i] = '\0';

return buffer;
}

/*****************************************************************************/

void AddTopicAssociation(struct TopicAssociation **list,char *fwd_name,char *bwd_name,char *topic_type,char *associates,int verify)

{ struct TopicAssociation *ta = NULL,*texist;
  char assoc_type[256];
  struct Rlist *rp;

strncpy(assoc_type,CanonifyName(fwd_name),255);


if (associates == NULL)
   {
   printf("A topic must have at least one associate in association %s",fwd_name);
   return;
   }

if ((texist = AssociationExists(*list,fwd_name,bwd_name,verify)) == NULL)
   {
   if ((ta = (struct TopicAssociation *)malloc(sizeof(struct TopicAssociation))) == NULL)
      {
      printf("malloc","Memory failure in AddTopicAssociation");
      exit(1);
      }
   
   if ((ta->fwd_name = strdup(fwd_name)) == NULL)
      {
      printf("Memory failure in AddTopicAssociation");
      exit(1);
      }

   ta->bwd_name = NULL;
       
   if (bwd_name && ((ta->bwd_name = strdup(bwd_name)) == NULL))
      {
      exit(1);
      }
   
   if (assoc_type && (ta->assoc_type = strdup(assoc_type)) == NULL)
      {
      exit(1);
      }

   ta->associates = NULL;
   ta->associate_topic_type = NULL;
   ta->next = *list;
   *list = ta;
   }
else
   {
   ta = texist;
   }

/* Association now exists, so add new members */

IdempPrependRScalar(&(ta->associates),associates,'s');
}

/*****************************************************************************/

struct TopicAssociation *AssociationExists(struct TopicAssociation *list,char *fwd,char *bwd,int verify)

{ struct TopicAssociation *ta;
  int yfwd = false,ybwd = false;
  char l[CF_BUFSIZE],r[CF_BUFSIZE];


if (fwd == NULL || (fwd && strlen(fwd) == 0))
   {
   exit(1);
   }


for (ta = list; ta != NULL; ta=ta->next)
   {
   if (strcmp(fwd,ta->fwd_name) == 0)
      {
      yfwd = true;
      }
   else if (fwd)
      {
      strncpy(l,ToLowerStr(fwd),255);
      strncpy(r,ToLowerStr(ta->fwd_name),255);
      }
   
   if (bwd && strcmp(bwd,ta->bwd_name) == 0)
      {
      ybwd = true;
      }
   else if (bwd && ta->bwd_name)
      {
      strncpy(l,ToLowerStr(bwd),255);
      strncpy(r,ToLowerStr(ta->bwd_name),255);
      }
   
   if (ta->bwd_name && strcmp(fwd,ta->bwd_name) == 0)
      {
      return ta;
      }

   if (bwd && strcmp(bwd,ta->fwd_name) == 0)
      {
      return ta;
      }

   if (yfwd && ybwd)
      {
      return ta;
      }
   
   if (yfwd && !ybwd)
      {
      return ta;
      }
   
   if (!yfwd && ybwd)
      {
      return ta;
      }
   }

return NULL;
}


/*******************************************************************/

struct Rlist *IdempPrependRScalar(struct Rlist **start,void *item, char type)

{ char *scalar = strdup((char *)item);

if (!KeyInRlist(*start,(char *)item))
   {
   return PrependRlist(start,scalar,type);
   }
else
   {
   return NULL;
   }
}


/*******************************************************************/

struct Rlist *KeyInRlist(struct Rlist *list,char *key)

{ struct Rlist *rp;

for (rp = list; rp != NULL; rp = rp->next)
   {
   if (strcmp((char *)rp->item,key) == 0)
      {
      return rp;
      }
   }

return NULL;
}

/*******************************************************************/

struct Rlist *PrependRlist(struct Rlist **start,void *item, char type)

   /* heap memory for item must have already been allocated */
    
{ struct Rlist *rp,*lp = *start;
  struct FnCall *fp;
  char *sp = NULL;

if ((rp = (struct Rlist *)malloc(sizeof(struct Rlist))) == NULL)
   {
   exit(1);
   }

rp->next = *start;
rp->item = strdup(item);
rp->type = type;  /* scalar, builtin function */

rp->state_ptr = NULL;

*start = rp;

return rp;
}

