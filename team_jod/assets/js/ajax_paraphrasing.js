
  $(document).ready(function(){

    var text_data = document.getElementById('original_text').value

    $(".paraphrasing_button").click(function(){
    alert("Hello")

      $.ajax({
      url:'/blogs/demo',
      type:'get',
      data:{
        data_content: text_data
      },
      success: function(response){
        alert(response.data)
      }
    });
    })




  })