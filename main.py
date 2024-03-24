import glfw
import OpenGL.GL as gl
from OpenGL.raw.GL.VERSION.GL_1_0 import GL_TRIANGLES


def main():
    # Initialize the library
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "Python window for GLFW", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL
        gl.glBegin(GL_TRIANGLES)
        gl.glVertex2d(0, 1)
        gl.glVertex2d(1, -1)
        gl.glVertex2d(-1, -1)
        gl.glEnd()
        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
