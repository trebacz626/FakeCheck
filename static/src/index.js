import Vue from 'vue';
import {store} from './store';
import BootstrapVue from 'bootstrap-vue';

Vue.component('account-balance-chart', require('./vue_components/AccountBalanceChart.vue').default);
Vue.component('account-select', require('./vue_components/AccountSelect.vue').default);
Vue.component('new-account', require('./vue_components/NewAccount.vue').default);
Vue.component('new-transaction', require('./vue_components/NewTransaction.vue').default);
Vue.component('account-balance-table', require('./vue_components/AccountBalanceTable.vue').default);
Vue.component('new-category', require('./vue_components/NewCategory.vue').default);
Vue.component('choice', require('./vue_components/Choice.vue').default);

Vue.use(BootstrapVue);
new Vue({
    el: "#app",
    store
});