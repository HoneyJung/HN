/*
cal.on("clickSchedule", function (event) {
  var schedule = event.schedule;
  lastClickSchedule = schedule;
  if (!lastClickSchedule) {
    cal.updateSchedule(lastClickSchedule.id, lastClickSchedule.calendarId, {
      isFocused: false,
    });
  }
  cal.updateSchedule(schedule.id, schedule.calendarId, {
    isFocused: true,
  });

  lastClickSchedule = schedule;
  // open detail view
});
cal.clear();
cal.on("clickDayname", function (event) {
  if (cal.getViewName() === "week") {
    cal.setDate(new Date(event.date));
    cal.changeView("day", true);
  }
});
*/

cal.on("clickSchedule", function (event) {
  var schedule = event.schedule;
  // open detail view
  // Get the modal

  modal_id = "myModal" + schedule.id;
  console.log(modal_id);
  var modal = document.getElementById(modal_id);

  // Get the button that opens the modal

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[schedule.id - 1];

  // When the user clicks on the button, open the modal
  modal.style.display = "block";

  // When the user clicks on <span> (x), close the modal
  span.onclick = function () {
    modal.style.display = "none";
  };

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };
});

cal.createSchedules([
  {
    id: "1",
    calendarId: "1",
    title: "2020 삼성 모니터 디자인 공모전",
    category: "time",
    dueDateClass: "",
    start: "2020-07-27T22:30:00+09:00",
    end: "2020-07-29T22:30:00+09:00",
    bgColor: "#ffffff",
  },
  {
    id: "2",
    calendarId: "1",
    title: "2020년 국민 생활문제 해결을 위한 솔‧직 챌린지",
    category: "time",
    dueDateClass: "",
    start: "2020-07-27T22:30:00+09:00",
    //end: '2018-01-19T02:30:00+09:00'
  },
  {
    id: "3",
    calendarId: "1",
    title: "LG 울트라기어 엠블럼 출시기념 팬아트 공모전",
    category: "time",
    dueDateClass: "",
    start: "2020-07-28T22:30:00+09:00",
    //end: '2018-01-19T02:30:00+09:00'
  },
  {
    id: "1",
    calendarId: "1",
    title: "2020 삼성 모니터 디자인 공모전",
    category: "time",
    dueDateClass: "",
    start: "2020-07-30T22:30:00+09:00",
    bgColor: "#000000",
    dragBgColor: "#000000",
    borderColor: "#000000",
  },
  {
    id: "2",
    calendarId: "1",
    title: "2020년 국민 생활문제 해결을 위한 솔‧직 챌린지",
    category: "time",
    dueDateClass: "",
    start: "2020-08-02T22:30:00+09:00",
    bgColor: "#000000",
    dragBgColor: "#000000",
    borderColor: "#000000",
  },
  {
    id: "3",
    calendarId: "1",
    title: "LG 울트라기어 엠블럼 출시기념 팬아트 공모전",
    category: "time",
    dueDateClass: "",
    bgColor: "#000000",
    dragBgColor: "#000000",
    borderColor: "#000000",
    start: "2020-08-14T22:30:00+09:00",
    //end: '2018-01-19T02:30:00+09:00'
  },
]);
