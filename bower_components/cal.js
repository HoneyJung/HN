var calendar = new tui.Calendar("#calendar", {
  defaultView: "month", // set 'month'
  month: {
    visibleWeeksCount: 2, // visible week count in monthly
  },
});

calendar.createSchedules([
  {
    id: "1",
    calendarId: "1",
    title: "서울시 BigData 공모전",
    category: "time",
    dueDateClass: "",
    start: "2020-06-28T22:30:00+09:00",
  },
  {
    id: "2",
    calendarId: "1",
    title: "대학생 광고 공모전",
    category: "time",
    dueDateClass: "",
    start: "2020-06-26T22:30:00+09:00",
  },
  {
    id: "3",
    calendarId: "1",
    title: "승강기 안전 공모전",
    category: "time",
    dueDateClass: "",
    start: "2020-06-26T22:30:00+09:00",
  },
  {
    id: "4",
    calendarId: "1",
    title: "2020 등대여행 영상 공모전",
    category: "time",
    dueDateClass: "",
    start: "2020-06-24T22:30:00+09:00",
  },
]);

calendar.setCalendarColor("1", {
  color: "#e8e8e8",
  bgColor: "#585858",
  borderColor: "#a1b56c",
  //dragBgColor: '#585858',
});
calendar.setCalendarColor("2", {
  color: "#282828",
  bgColor: "#dc9656",
  borderColor: "#a1b56c",
  //dragBgColor: '#dc9656', 왜 없어?
});
calendar.setCalendarColor("3", {
  color: "#a16946",
  bgColor: "#ab4642",
  borderColor: "#a1b56c",
  //dragBgColor: '#ab4642',
});
