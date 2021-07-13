// module.exports = new Vue({
export default new Vue({
    data: {
        items: [
            {id: 1, name: '親1', children: [
                {id: 11, name: '子1', children: []},
                {id: 12, name: '子2', children: []}
            ]},
            {id: 2, name: '親2', children: [
                {id: 21, name: '子3', children: []},
                {id: 22, name: '子4', children: []}
            ]}
        ]
    },
    methods: {
        getItems: function() {
            return this.items;
        },
        setItems: function(val) {
            this.items = val;
        }
    },
    setMethods: function() {
        return this.methods;
    }
});