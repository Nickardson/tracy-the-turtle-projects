import webgl
from math import sin

gl = webgl.Context("webgl-canvas")
trianglesVerticeBuffer = gl.createBuffer()
trianglesColorBuffer = gl.createBuffer()
program = None
uViewMatrix = None
uProjMatrix = None
viewMatrix = webgl.Matrix4x4([1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0])
projMatrix = webgl.Matrix4x4([1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0])

def setup():
  print viewMatrix
  print projMatrix
  global program, uViewMatrix, uProjMatrix
  vs = gl.createShader(gl.VERTEX_SHADER) 
  gl.shaderSource(vs, "" + 
  "attribute vec3 aVertexPosition;" + 
  "attribute vec3 aVertexColor;" +
  "" +
  "uniform mat4 uViewMatrix;" +
  "uniform mat4 uProjMatrix;" +
  "" + 
  "varying highp vec4 vColor;" + 
  "void main(void) {" + 
  "  gl_Position = uProjMatrix * uViewMatrix * vec4(aVertexPosition, 1.0);" + 
  "  vColor = vec4(aVertexColor, 1.0);" + 
  "}")
  gl.compileShader(vs)
  print "Vertex shader COMPILE_STATUS: " + str(gl.getShaderParameter(vs, gl.COMPILE_STATUS))
  fs = gl.createShader(gl.FRAGMENT_SHADER) 
  gl.shaderSource(fs, "" + 
  "varying highp vec4 vColor;" + 
  "void main(void) {" + 
  "  gl_FragColor = vColor;" + 
  "}")
  gl.compileShader(fs)
  print "Fragment shader COMPILE_STATUS: " + str(gl.getShaderParameter(fs, gl.COMPILE_STATUS))

  program = gl.createProgram()
  gl.attachShader(program, vs)
  gl.attachShader(program, fs)
  gl.linkProgram(program)
  print "Program LINK_STATUS: " + str(gl.getProgramParameter(program, gl.LINK_STATUS))
  gl.useProgram(program)

  triangleVerticeColors = [1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0]

  gl.bindBuffer(gl.ARRAY_BUFFER, trianglesColorBuffer)
  gl.bufferData(gl.ARRAY_BUFFER, webgl.Float32Array(triangleVerticeColors), gl.STATIC_DRAW)

  uViewMatrix = gl.getUniformLocation(program, "uViewMatrix")
  uProjMatrix = gl.getUniformLocation(program, "uProjMatrix")
  projMatrix.perspective(45, 4.0/3.0, 0.1, 100.0)
  viewMatrix.identity()
  viewMatrix.translate([0.0, 0.0, -2.0])
  gl.clearColor(0.0, 0.0, 0.0, 1.0);  
  gl.viewport(0, 0, 400, 300);

def draw(gl, elapsed):
  gl.clear(gl.COLOR_BUFFER_BIT);  
  translation = sin(elapsed * 2.0 * 3.14159 / 10000.0)/2.0;
  triangleVertices = [-0.5 + translation,  0.5, -0.5,
                       0.0 + translation,  0.0, -0.5,
                      -0.5 + translation, -0.5, -0.5,
                       0.5 + translation,  0.5,  0.5,
                       0.0 + translation,  0.0,  0.5,
                       0.5 + translation, -0.5,  0.5]
  gl.bindBuffer(gl.ARRAY_BUFFER, trianglesVerticeBuffer)
  gl.bufferData(gl.ARRAY_BUFFER, webgl.Float32Array(triangleVertices), gl.DYNAMIC_DRAW)

  gl.uniformMatrix4fv(uProjMatrix, False, projMatrix)
  gl.uniformMatrix4fv(uViewMatrix, False, viewMatrix)

  vertexPositionAttribute = gl.getAttribLocation(program, "aVertexPosition")
  gl.enableVertexAttribArray(vertexPositionAttribute)
  gl.bindBuffer(gl.ARRAY_BUFFER, trianglesVerticeBuffer)
  gl.vertexAttribPointer(vertexPositionAttribute, 3, gl.FLOAT, False, 0, 0)

  vertexColorAttribute = gl.getAttribLocation(program, "aVertexColor")
  gl.enableVertexAttribArray(vertexColorAttribute)
  gl.bindBuffer(gl.ARRAY_BUFFER, trianglesColorBuffer)
  gl.vertexAttribPointer(vertexColorAttribute, 3, gl.FLOAT, False, 0, 0)

  gl.drawArrays(gl.TRIANGLES, 0, 6)

setup()

gl.setDrawFunc(draw);