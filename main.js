var app = new Vue({

	el: '#app',

	data: {

		title: "SSDS T&E Acronyms",

		word: null,

		buttonFlag: false

	},

	methods: {

		findAcronym() {
			pythonMethod_findAcronym(this.word)
		}

		}
})







