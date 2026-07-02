---
titulo: "Sticky Header Code"
fecha: 2024-02-06
mensajes: 2
origen: ChatGPT
---

# Sticky Header Code

### Usuario

Show me a code snippet of a website's sticky header in CSS and JavaScript.

### Asistente

Sure, here's a simple example of how you can create a sticky header for a website using CSS and JavaScript:

HTML:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sticky Header Example</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

<header id="header">
  <!-- Your header content goes here -->
  <h1>My Sticky Header</h1>
</header>

<!-- Main content of the website -->
<main>
  <p>This is the main content of the website.</p>
</main>

<script src="script.js"></script>
</body>
</html>
```

CSS (styles.css):
```css
/* Styles for the header */
#header {
  background-color: #333;
  color: #fff;
  padding: 10px 0;
  text-align: center;
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1000; /* Ensure the header stays on top */
}

/* Styles for the main content */
main {
  padding-top: 50px; /* Ensure content doesn't get covered by the fixed header */
}
```

JavaScript (script.js):
```javascript
// JavaScript to add a class when scrolling down
window.addEventListener('scroll', function() {
  var header = document.getElementById('header');
  if (window.scrollY >
