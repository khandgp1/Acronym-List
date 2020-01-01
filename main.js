var app = new Vue({

	el: '#app',

	data: {

		title: "SSDS T&E Acronyms",
		word: null,
		test: null

	},

	methods: {

		findAcronym() {
			axios
				.get('http://localhost:5000/acronymnList/' + this.word)
				.then(response => (this.test = response.data.acronymn))		
		},
		test() {
			this.test = "letsdoit"
		}
	}
})
  
  





