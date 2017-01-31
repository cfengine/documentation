/*****************************************************************************/
/*                                                                           */
/* File: highlight_syntax.c                                                  */
/*                                                                           */
/* Created: Tue Nov 23 17:59:10 2010                                         */
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

void HighlightManual(char *file);
void ProcessFile(char *document,FILE *fin);
void TransformLine(char *line,FILE *fout);
int IsFunction(char *s);

main(int argc, char **argv)

{
// Prefix for Web pages:  http://cfengine.com/inside/manuals/
// Prefix for Nova, etc: /

HighlightManual(argv[1]);
}

/*****************************************************************************/

void HighlightManual(char *file)

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
strcat(name,".trans");

ProcessFile(name,fin);

fclose(fin);
}

/*****************************************************************************/

void ProcessFile(char *document,FILE *fin)

{ char tmp[2048],line[2048],type[2048],url[2048],title[2048],*sp;
  int code = false;  
  FILE *fout;
  
if ((fout = fopen(document,"w")) == NULL)
   {
   printf("File missing\n");
   exit(0);
   }

while (!feof(fin))
   {
   fgets(line,2047,fin);

   if (sp = strstr(line,"<pre class=\"verbatim\">"))
      {
      code = true;
      fprintf(fout,"%s",line);
      continue;
      }
   else if (sp = strstr(line,"</pre>"))
      {
      code = false;
      fprintf(fout,"%s",line);
      continue;
      }

   if (code)
      {
      TransformLine(line,fout);
      }
   else
      {
      fprintf(fout,"%s",line);
      }
   }

fclose(fout);
}

/***************************************************/

void TransformLine(char *line,FILE *fout)

{ char *sp,*spt,*spf;
 char newline[4096] = {0},lhs[2000] = {0},rhs[2000] = {0},ud[2000] = {0};
  char lhs1[2000] = {0},lhs2[2000] = {0};
  char sstring[1000] = {0};
  
sscanf(line,"%s",sstring);

if (*sstring == '#')
   {
   fprintf(fout,"<span class=\"comment\">%s</span>\n",line);
   return;
   }
  
if (strstr(line,"=>"))
   {
   if (*sstring == '\"')
      {
      int offset = 0,count = 0;

      sstring[0] = '\0';

      for (spf = line,spt = sstring; *spf != '\0'; spf++,spt++)
         {
         *spt = *spf;
         
         if (*spf == '\"')
            {
            count++;
            }

         if (count == 2)
            {
            *(spt+1) = '\0';
            break;
            }
         }

      fprintf(fout,"%s",sstring);
      line += strlen(sstring);
      }

   sstring[0] = '\0';
   sscanf(line,"%[^=]=>%[^\n]",lhs,rhs);
   sscanf(rhs,"%s",sstring);

   lhs1[0] = '\0';
   lhs2[0] = '\0';
   
   sscanf(lhs,"%[^\"]\"%[^\n]",lhs1,lhs2);

   if (strlen(lhs1)==strlen(lhs))
      {
      strcpy(lhs2,lhs);
      lhs1[0] = '\0';
      }
   else
      {
      strcat(lhs1,"\"");
      }
   
   if (*sstring == '\"')
      {
      fprintf(fout,"%s<span class=\"red\">%s</span>=><span class=\"green\">%s</span>\n",lhs1,lhs2,rhs);
      }
   else if (strchr(rhs,'{') || IsFunction(rhs))
      {
      fprintf(fout,"<span class=\"red\">%s</span>=>%s\n",lhs,rhs);
      }
   else
      {
      fprintf(fout,"%s<span class=\"red\">%s</span>=><span class=\"blue\">%s</span>\n",lhs1,lhs2,rhs);
      }
    }
else if (strstr(line,"body") || strstr(line,"bundle"))
   {
   if (strstr(line,"common"))
      {
      fprintf(fout,"<span class=\"red\">%s</span>",line);
      }
   else
      {
      sscanf(line,"%s %s %s",lhs,rhs,ud);
      fprintf(fout,"<span class=\"red\">%s %s</span> <span class=\"blue\">%s</span>\n",lhs,rhs,ud);
      }
   }
else if (strchr(line,':') && !strstr(line,"::"))
   {
   fprintf(fout,"<span class=\"red\">%s</span>",line);
   }
else
   {
   fprintf(fout,"%s",line);
   }
}

/***************************************************/

int IsFunction(char *s)

{ int i;
 char *fns[] = { "accessedbefore",
                 "accumulated",
                 "ago",
                 "canonify",
                 "changedbefore",
                 "classify",
                 "classmatch",
                 "countclassesmatching",
                 "countlinesmatching",
                 "diskfree",
                 "escape",
                 "execresult",
                 "fileexists",
                 "filesexist",
                 "getenv",
                 "getfields",
                 "getgid",
                 "getindices",
                 "getuid",
                 "getusers",
                 "grep",
                 "groupexists",
                 "hash",
                 "hashmatch",
                 "host2ip",
                 "hostinnetgroup",
                 "hostrange",
                 "hostsseen",
                 "hubknowledge",
                 "iprange",
                 "irange",
                 "isdir",
                 "isexecutable",
                 "isgreaterthan",
                 "islessthan",
                 "islink",
                 "isnewerthan",
                 "isplain",
                 "isvariable",
                 "join",
                 "lastnode",
                 "laterthan",
                 "ldaparray",
                 "ldaplist",
                 "ldapvalue",
                 "now",
                 "on",
                 "peers",
                 "peerleader",
                 "peerleaders",
                 "product",
                 "randomint",
                 "readfile",
                 "readintarray",
                 "readintlist",
                 "readrealarray",
                 "readreallist",
                 "readstringarray",
                 "readstringarrayidx",
                 "readstringlist",
                 "readtcp",
                 "regarray",
                 "regcmp",
                 "regextract",
                 "registryvalue",
                 "regline",
                 "reglist",
                 "regldap",
                 "remotescalar",
                 "remoteclassesmatching"
                 "returnszero",
                 "rrange",
                 "selectservers",
                 "splayclass",
                 "splitstring",
                 "strcmp",
                 "sum",
                 "translatepath",
                 "usemodule",
                 "userexists",
                 NULL
                 };

 for (i = 0; fns[i] != NULL; i++)
    {
    if (strstr(s,fns[i]))
       {
       return true;
       }
    }
 
return false;
}

