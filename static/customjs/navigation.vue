<template>
    <v-treeview
        mandatory
        activatable
        :items="items"
        :return-object="true"
        @update:active="update"
    ></v-treeview>
</template>

<script>
    export default {
        props: [ "items" ],
        methods: {
			update: function(nodes) {
                this.$emit("node-click");
        	},
        }
    }
</script>