#include <windows.h>
#include <GL/glut.h>
#include <GL/glu.h>
#include <GL/gl.h>


using namespace std;
void init()
{


    glClearColor(1,1,1,0);
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(0.0,200,0.0,400);
    glPointSize(10.0);
}

void mypoint()
{
    glClear(GL_COLOR_BUFFER_BIT);

    glBegin(GL_POINTS);
        glColor3f(1,0,0);
        glVertex2f(10.0,10.0);
        glColor3f(0,1,0);
        glVertex2f(10.0,70.0);
        glColor3f(0,0,1);
        glVertex2f(100.0,70.0);
        glColor3f(1,1,0);
        glVertex2f(100.0,10.0);
    glEnd();

    glFlush();

}


int main(int argc, char **argv)
{

    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
    glutCreateWindow("Motherfucker");
    glutInitWindowSize(300,400);
    glutInitWindowPosition(10,30);

    init();
    glutDisplayFunc(mypoint);
    glutMainLoop();
}
