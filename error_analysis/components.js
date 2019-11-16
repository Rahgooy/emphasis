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
  template: '<span :style=x.getStyle()>{{x.word}}</span>'
});
