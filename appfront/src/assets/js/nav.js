$(function () {
  startTime();
  function startTime() {
    var today=new Date();
    var y=today.getFullYear();
    var M=today.getMonth()+1;
    var d=today.getDate();
    var h=today.getHours();
    var m=today.getMinutes();
    var s=today.getSeconds();
    m=checkTime(m);
    s=checkTime(s);
    $('#time').html(+h+':'+m+':'+s);
    $('#date').html(y+'-'+M+'-'+d);
    t=setTimeout(startTime,500);
    function checkTime(i) {
      if (i<10){
        i="0"+i;
      }
      return i;
    }
  }





})

