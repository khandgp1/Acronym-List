var app = new Vue({

	el: '#app',

	data: {

		title: "SSDS T&E Acronyms",
		word: "SSDS",
		description: "Ship Self-Defense System",
		test: null

	},

	methods: {

		findAcronym() {
			axios
				.get('http://localhost:5000/acronymnList/' + this.word)
				.then(response => (this.test = response.data.acronymn))		
		},
		findword() {
			this.test = "letsdoit"
		}
	}
})
  
  





