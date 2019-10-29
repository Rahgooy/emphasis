Vue.component('model', {
  props: ['m'],
  template: '<li :style=m.style>{{m.name}}</li>'
});
Vue.component('sample', {
  props: ['s'],
  template: '<div><span v-for="x in s"><highlight :x="x"></highlight>&nbsp</span></div>'
});
Vue.component('highlight', {
  props: ['x'],
  template: '<span :style=x.style>{{x.word}}</span>'
});
new Vue({
  el: '#app',
  data: {
    samples: 0,
    page: 0,
    models: [],
    COLORS: ['red', 'blue', 'brown', 'aqua', 'black', 'maroon']
  },
  methods: {
    show_help: function() {
      msg =  "1. Load the ground-truth file by clicking on 'add-ground-truth' button\n" +
      "2. Load a model file by clicking on 'add-model' button\n" +
      "3. Navigate through the samples";
      alert(msg);
    },
    goto_page: function(e) {
      index = parseInt(e.target.value) - 1;
      if(index >=0 && index < this.samples){
        this.page = index;
      }
    },
    next_page: function() {
      if (this.page < this.samples - 1)
        this.page++;
    },
    prev_page: function() {
      if (this.page > 0)
        this.page--;
    },
    add_ground_truth: function() {
      Reader((data, filename) => {
        if (!data.length || data[0][0].pos == '') {
          alert('Invalid ground-truth data!');
          return;
        }
        this.samples = data.length;
        m = {
          id: 0,
          name: '[gt] ' + filename,
          data: data,
          type: 'gt',
          style: {
            color: 'green'
          }
        };
        if (!this.models.length)
          this.models.push(m);
        else if (this.models[0].type == 'gt')
          this.models[0] = m;
        else
          this.models.unshift(m)
      });
    },
    add_model: function() {
      if (!this.models.length) {
        alert('Please load the ground-truth first.');
        return;
      }
      Reader((data, filename) => {
        if (!validate(this.models[0].data, data)) {
          alert('Data is not matching with the ground-truth.');
          return;
        }
        this.models.push({
          id: this.models.length + 1,
          name: '[model] ' + filename,
          data: data,
          type: 'model',
          style: {
            color: this.COLORS[this.models.length % 6]
          }
        });
      });
    }
  }
});
