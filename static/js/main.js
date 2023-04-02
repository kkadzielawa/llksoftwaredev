fetch("/courses/config/")
    .then((result) => { return result.json(); })
    .then((data) => {
        const stripe = Stripe(data.publicKey);
        console.log(stripe)
    });