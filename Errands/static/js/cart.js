var updateBtns = document.getElementsByClassName('update_cart')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)

        console.log('USER', user)
        if (user == 'AnonymousUser') {
            console.log('User is not authenticated')
        }else{
            console.log('User is authenticated, sending data...')
        }

    })
}