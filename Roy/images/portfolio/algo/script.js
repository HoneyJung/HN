function submit () {
    console.log("hi")
	fetch('./index',  {
		method: 'post',
		headers: {'Content-Type': 'application/json'},
		body: JSON.stringify({ })
	})
        .then(req => {
            req.json();
            console.log(req)
        }
        )
		.then(ret => {
    
			// Update Element
		});
};
