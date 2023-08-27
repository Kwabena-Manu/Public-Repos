#include <windows.h>
#include <GL/glut.h>
#include <GL/glu.h>
#include <GL/gl.h>
#include <math.h>

using namespace std;
#define WIDTH 640
#define HEIGHT 480
//Laryea Frandy Odai Index Number 1652717

void reshape(int width, int height){
glViewport(0,0,width,height);
glMatrixMode(GL_PROJECTION);
glLoadIdentity();
glOrtho(-WIDTH/2,WIDTH/2-1,-HEIGHT/2,HEIGHT/2-1,-1,1);
glMatrixMode(GL_MODELVIEW);
glLoadIdentity();
}
void Timer(int ex)
{
glutPostRedisplay();
glutTimerFunc(30,Timer,0);
}
void init()
{

    glClearColor(1,1,1,1);

    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(0,160,0,120);
    glPointSize(2.0);

}
#define PI 3.142

GLint circle_points = 100;
void mycircle(GLfloat centerx, GLfloat centery, GLfloat radius)
{




    glClear(GL_COLOR_BUFFER_BIT);

    glBegin(GL_POLYGON);

        GLdouble theta;
        for(GLint i=0;i<circle_points;i++)
        {

            theta = 2*PI*i/circle_points; //in radians

            glVertex2f((centerx+radius*cos(theta)),(centery+radius*sin(theta)));


        }
    glEnd();



}


void Display()
{
    GLint radius = 40;

    GLint xpos = 60;
    GLint ydir =1;
    GLint ypos = ypos + 1.5*ydir;

    if (ypos == 120-radius)
        ydir = ydir *-1;
    else if (ypos <radius)
        ydir = ydir *-1;

    glLoadIdentity();
    glTranslatef(xpos,ypos,0);






    glColor3f(0.1,0.2,0.5);
    mycircle(0,0,radius);

    glutSwapBuffers();
    glutPostRedisplay();

    glFlush();

}

int main(int argc, char **argv)
{

    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB);
    glutInitWindowSize(500,600);
    glutInitWindowPosition(10,10);
    glutCreateWindow("Another motherfucker");

    init();
    glutDisplayFunc(Display);
    glutReshapeFunc(reshape);
    glutTimerFunc(0,Timer,600);

    glutMainLoop();

}
