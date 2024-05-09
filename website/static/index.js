function deleteAccount(phoneNumb){
    fetch('/delete-acc',{
        method: 'POST',
        body: JSON.stringify({phoneNumb:phoneNumb})
    }).then((_res) => {
        window.location.href="/";
    });
}