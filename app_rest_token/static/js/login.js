

document.getElementById('submit').addEventListener('click',verify_data);
function verify_data(event){
    event.preventDefault();    
    document.getElementById('reg_form').classList.add('was-validated');
    post_data = {
        'username':document.getElementById('username').value,
        'password':document.getElementById('password').value
    };
    $.ajax({
        url:'../custom_token/',
        type: "POST",
        headers: {'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value},
        data: post_data,
        success: function (res) {
            if (res.status){
                console.log(res)
            }
            else{
                console.log(res)
            }
        },

        // Error handling 
        error: function (error) {
            console.log(`Error ${error}`);
        }
    });
}