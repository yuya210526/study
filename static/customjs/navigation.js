import Nodes from './nodes.js';

Vue.component('my-navigation', require('./navigation.vue'));

const navigation = new Vue({
    el: '#navigation',
    data: Nodes.$data,
    methods: {
        select: function() {
            if(nodes.length){
                  document.getElementById('select_node2').innerHTML = nodes[0].name + ' が選択されました。';
            } else {
                  document.getElementById('select_node2').innerHTML = '選択が解除されました。';
            }
        }
    }
});