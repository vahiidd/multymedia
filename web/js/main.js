document.getElementById('audio').addEventListener(
  'click',
  () => {
    eel.audio();
  },
  false
);
document.getElementById('image').addEventListener(
  'click',
  () => {
    eel.image();
  },
  false
);
document.getElementById('button-date').addEventListener(
  'click',
  () => {
    eel.get_date();
  },
  false
);
document.getElementById('button-ip').addEventListener(
  'click',
  () => {
    eel.get_ip();
  },
  false
);

eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}
