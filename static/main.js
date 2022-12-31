document.addEventListener("DOMContentLoaded", () => {
  const slider = document.querySelector("#durationSlider");
  const speed = document.querySelector("#speed");
  const durationValue = parseInt(document.querySelector("#duration").innerHTML);
  const duration = document.querySelector("#duration");

  duration.innerHTML = hhmmssFormat(
    Math.round(10 * parseFloat(duration.innerHTML)) / 10
  );

  slider.addEventListener("input", (e) => {
    let value = slider.value;
    speed.innerHTML = value;

    duration.innerHTML = hhmmssFormat(
      Math.round((durationValue * 10) / parseFloat(value)) / 10
    );

    e.preventDefault();
  });
});

function hhmmssFormat(givenSeconds) {
  dateObj = new Date(givenSeconds * 1000);
  hours = dateObj.getUTCHours();
  minutes = dateObj.getUTCMinutes();
  seconds = dateObj.getSeconds();

  timeString =
    hours.toString().padStart(2, "0") +
    ":" +
    minutes.toString().padStart(2, "0") +
    ":" +
    seconds.toString().padStart(2, "0");

  return timeString;
}
