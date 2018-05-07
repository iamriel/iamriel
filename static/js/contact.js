var app = new Vue({
  el: '#contact',
  data: {
    loading: false,
    form: {
      email: '',
      subject: '',
      message: ''
    },
    errors: {},
    successMessage: ''
  },
  methods: {
    clearFormData () {
      this.form = {
        email: '',
        subject: '',
        message: ''
      };
    },
    submit () {
      this.loading = true;
      this.successMessage = '';
      var formData = this.form;
      formData.csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();

      $.post('/contact/', formData,
        (data) => {
          this.errors = {};
          this.clearFormData();
          this.loading = false;
          this.successMessage = data.message;
          console.log(data);
        }
      ).fail((error) => {
        this.errors = error.responseJSON;
        this.loading = false;
      });
    },
    formGroupClass (name) {
      return {
        'form-group': true,
        'has-error': this.errors[name]
      };
    }
  }
});
