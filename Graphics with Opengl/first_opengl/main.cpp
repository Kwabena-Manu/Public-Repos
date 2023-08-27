#include<windows.h>
#include <GL/glu.h>
#include <GL/glut.h>
void mydisplay()
{
 glClear(GL_COLOR_BUFFER_BIT);
glColor3f(1.0, 0.0, 0.0);
 glBegin(GL_POLYGON);
glVertex2f(-0.5, -0.5);
glVertex2f(-0.5, 0.5);
glVertex2f(0.5, 0.5);
glVertex2f(0.5, -0.5);
 glEnd();
glFlush();
}
int main()
{
glutCreateWindow("simple");
glutDisplayFunc(mydisplay);
glutMainLoop();
return 0;
}
