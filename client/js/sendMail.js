function sendMail(event){
  event.preventDefault();
  var form = document.getElementById("mail");
  var data = new FormData(form);
  console.log(data)

}
