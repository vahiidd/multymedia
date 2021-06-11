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
document.getElementById('video').addEventListener(
  'click',
  () => {
    eel.video();
  },
  false
);
// eel.expose(prompt_alerts);
// function prompt_alerts(description) {
//   alert(description);
// }
