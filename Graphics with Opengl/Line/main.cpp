#include <windows.h>
#include <GL/glut.h>
#include <GL/glu.h>
#include <GL/gl.h>


using namespace std;

void init ()
{

    glClearColor(0.2,0.4,0.8,0);
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(0.0,40,0.0,50);

}

void mypic()
{

    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(0.3,0.0,0.0);
    glBegin(GL_LINES);
        glVertex2i(0,0);
        glVertex2i(40,50);
    glEnd();

    glFlush();

}

int main(int argc,char **argv)
{
    glutInit(&argc,argv);
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
    glutInitWindowPosition(200,100);
    glutInitWindowSize(500,600);
    glutCreateWindow("My Image");
    init();

    glutDisplayFunc(mypic);

    glutMainLoop();

    return 0;
}
