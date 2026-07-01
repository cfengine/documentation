/*****************************************************************************/
/*                                                                           */
/* File: scan_examples.c                                                     */
/*                                                                           */
/* Created: Sun Jun 14 09:05:07 2009                                         */
/*                                                                           */
/*****************************************************************************/

#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <dirent.h>

#define CF_SCALAR 's'

#define false 0
#define true  1
#define CF_BUFSIZE 2048
#define cf_error 1

FILE *FOUT;
char *CanonifyName(char *str);
void ProcessFile(char *file,FILE *fin);
void Convert(char *file);
void DocumentFile(char *filename,char *m);

char *SRC = "../../core/examples";

/*****************************************************************************/

main(int argc, char **argv)

{ DIR *dirh;
 struct dirent *dirp;

if ((FOUT = fopen("examples.cf","w")) == NULL)
   {
   printf("Can't open\n");
   exit(0);
   }

fprintf(FOUT,"bundle knowledge examples\n{\n");

if ((dirh = opendir(SRC)) == NULL)
   {
   perror("opendir");
   return false;
   }

for (dirp = readdir(dirh); dirp != NULL; dirp = readdir(dirh))
   {
   if (*(dirp->d_name) == '.')
      {
      continue;
      }

   if (strstr(dirp->d_name,"~"))
      {
      continue;
      }

   if (strstr(dirp->d_name,".txt"))
      {
      continue;
      }
   if (strstr(dirp->d_name,".html"))
      {
      continue;
      }
   
   if (strstr(dirp->d_name,"README"))
      {
      continue;
      }

   if (strstr(dirp->d_name,"Makefile"))
      {
      continue;
      }

   Convert(dirp->d_name);
   }


fprintf(FOUT,"\n}\n");
closedir(dirh);
fclose(FOUT);
}

/*****************************************************************************/

void Convert(char *file)

{ FILE *fin;
  char name_src[2048],name_hints[2048],name_out[2048];

/* Start with the main doc file */

 snprintf(name_src,2048,"%s/%s",SRC,file);
  
if ((fin = fopen(name_src,"r")) == NULL)
   {
   printf("File missing %s\n",name_src);
   exit(0);
   }

printf(" Examining %s\n",file);

strcpy(name_out,file);
*(strchr(name_out,'.')) = '\0'; // strip extension
strcat(name_out,".html");

printf(" Want to make %s\n",name_out);

ProcessFile(name_out,fin);

snprintf(name_hints,2048,"Units/%s",file);

DocumentFile(name_hints,name_out);
fclose(fin);
}

/*****************************************************************************/

void ProcessFile(char *file,FILE *fin)

{ int lineno = 0;  
  FILE *fout,*fin2;
  char topic[1024],subtype[1024],line[2048],qtopic[1024],*sp;

if ((fout = fopen(file,"w")) == NULL)
   {
   printf("Can't open %s\n",file );
   exit(0);
   }

printf(" Creating %s\n",file);


fprintf(fout," <div id=\"wholebody\"><div id=\"pagebody\"><div class=\"rtop\"><div class=\"r1\"></div><div class=\"r2\"></div><div class=\"r3\"></div><div class=\"r4\"></div></div><div id=\"content\">\n<pre>\n");

fprintf(fout,"<h1>Cfengine 3 example %s</h1>\n",file);

while (!feof(fin))
   {
   fgets(line,2047,fin);
   lineno++;

   if (strncmp(line,"#cop",4) == 0)
      {
      sscanf(line,"#cop %[^,],%[^\n]",qtopic,subtype);

      for (sp = qtopic; *sp != '\0'; sp++)
         {
         if (*sp == '(')
            {
            *sp = '\0';
            break;
            }
         }
      
      if (strstr(qtopic,"::"))
         {
         strcpy(topic,strchr(qtopic,':')+2);
         }
      else
         {
         strcpy(topic,qtopic);
         }

      printf("Processing %s\n",file);
      fprintf(FOUT,"occurrences:\n   %s::\n \"/showexample/example/%s\" represents => { \"%s\" };\n",CanonifyName(topic),file,subtype);
      continue;
      }

   fprintf(fout,"%s",line);
   }

fprintf(fout,"</div><div class=\"rbottom\"><div class=\"r4\"></div><div class=\"r3\"></div><div class=\"r2\"></div><div class=\"r1\"></div></div></div></div></div>");
fclose(fout);
}

/*****************************************************************************/

void DocumentFile(char *filename,char *outname)

{ int lineno = 0;  
  FILE *fout,*fin;
  char topic[1024],subtype[1024],line[2048],qtopic[1024],*sp;

  printf("Document file %s\n",filename);
  
if ((fin = fopen(filename,"r")) == NULL)
   {
   printf("warning - File processed missing %s \n",filename);
   return;
   }

while (!feof(fin))
   {
   fgets(line,2047,fin);
   lineno++;

   if (strncmp(line,"#cop",4) == 0)
      {
      sscanf(line,"#cop %[^,],%[^\n]",qtopic,subtype);

      for (sp = qtopic; *sp != '\0'; sp++)
         {
         if (*sp == '(')
            {
            *sp = '\0';
            break;
            }
         }
      
      if (strstr(qtopic,"::"))
         {
         strcpy(topic,strchr(qtopic,':')+2);
         }
      else
         {
         strcpy(topic,qtopic);
         }
      
      fprintf(FOUT,"occurrences:\n   %s::\n \"/showexample/example/%s\" represents => { \"%s\" };\n",CanonifyName(topic),outname,subtype);
      continue;
      }
   }

fclose(fout);
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

