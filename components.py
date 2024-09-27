# html
def printColored(text, color="blake", size=20):
  return f'<p id="idText" style="font-size: {size}; color: {color} ;"> {text} </p>'

def printGreen(text, size_font=50):
  return printColored(text, "green", size_font)

def printRed(text, size_font=50):
  return printColored(text, "red", size_font)

def printBlue(text, size_font=50):
  return printColored(text, "blue", size_font)

def createTextInputConnection(size=20):
  return f'<input type="text" id="urlInput" placeholder="Enter your name" style="margin-right: 10px; padding: 5px; font-size: {size}px;">'

def createButtonConnection(text, color="blake", size=20):
  return f'<button style="font-size: {size}px; color: {color}; padding: 10px 20px;" onclick="redirect()">{text}</button>'


# js
def createRedirectScript():
  return '''
  <script>
    function redirect() {
      let url = document.getElementById('urlInput').value.toLowerCase();
      if (url) {
        window.location.href = '/login/' + url;
      }
    }
  </script>
  '''