const meetingInput = document.querySelector(".meeting-input input");
const nextbutton = document.querySelector("#send-meeting");

nextbutton.addEventListener("click", (e) => {
    let meetingdata = meetingInput.value.trim();
    let date = new Date().toISOString();
    let meetinginfo = { date: date, meeting: meetingdata};
    let meetingjson = JSON.stringify(meetinginfo)
    if (meetingdata) {
        console.log(meetingjson);
        $.ajax({
            url: '/meeting',
            type: 'POST',
            data: meetingjson,
            contentType: 'application/json; charset=utf-8',
            success: function (response) {
                alert("Meeting info saved !! Click next to add prompts");
            },
            error: function() {
                alert("error");
            }
        });
        localStorage.setItem("meeting-info", meetingjson);
    }
  });