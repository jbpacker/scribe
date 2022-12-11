const generateButton = document.querySelector("#generate-summary");

generateButton.addEventListener("click", (e) => {
        $.ajax({
            url: '/summary',
            type: 'GET',
            contentType: 'application/json; charset=utf-8',
            beforeSend: function() {
              $('#loader').removeClass('hidden')
            },
            success: function (response) {
              console.log(response);
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