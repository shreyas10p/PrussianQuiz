const vue = new Vue({
    el: '#signup-button',
    methods:{
        goToSignUp(){
            console.log(this.$el.getAttribute('url_id'))
            window.location.href = this.$el.getAttribute('url_id')
           }
    }
})

const loginpost = new Vue({
    el: '#login-form',
    data: {
        username: null,
        password: null,

      },
    methods:{
        submitForm(){
            axios({
                method : "POST",
                url:this.$el[1].value, 
                headers: {'X-CSRFTOKEN': this.$el[0].value, 'Content-Type': 'application/json'},
                data : {"username":this.$el[2].value, "password":this.$el[3].value},
              }).then(response => {
                window.location.href = response.data['next']
              }).catch(err => {
                    console.log(err.response.data['err']);
              });
        }
    }
})

const app = new Vue({
    el: 'input#id_birth_date',
    components: {
        vuejsDatepicker
    }
  })