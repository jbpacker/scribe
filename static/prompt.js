const generateButton = document.querySelector("#generate-summary");
const summaryarea = document.querySelector("#summary")

generateButton.addEventListener("click", (e) => {
        $.ajax({
            url: '/summary',
            type: 'GET',
            contentType: 'application/json; charset=utf-8',
            beforeSend: function() {
              $('#loader').removeClass('hidden')
            },
            success: function (response) {
              console.log(response.result);
              summaryarea.innerHTML = response.result;
            },
            complete: function(){
              $('#loader').addClass('hidden')
          },
            error: function() {
                alert("error");
            }
        });
    }
  );
