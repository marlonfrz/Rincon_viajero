window.addEventListener("load", function(){
  window.cookieconsent.initialise({
    "palette": {
      "popup": {
        "background": "#fbf1e9"
      },
      "button": {
        "background": "#107acc"
      }
    },
    "theme": "wire",
    "content": {
      "message": "Este sitio web utiliza cookies para garantizar que obtenga la mejor experiencia en nuestro sitio web.",
      "dismiss": "Aceptar",
      "link": "Leer más",
      "href": "{% url 'posts:cookies_policy' %}"
    },
    "onStatusChange": function(status) {
      if (this.hasConsented()) {
        gtag('consent', 'default', {
          'analytics_storage': 'denied'
        });
      }
    }
  });
});
