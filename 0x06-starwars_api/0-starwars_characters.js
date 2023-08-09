#!/usr/bin/node

// Star Wars Characters

const request = require('request')
id = process.argv[2]
url = `https://swapi-api.alx-tools.com/api/films/${id}`
request(url, (err, res, body) => {
    data = JSON.parse(body)
    characters = data["characters"]
    for (const character of characters) {
        request(character, (error, resp, bodyy) => {
            console.log(JSON.parse(bodyy)["name"])
        })
    }
})
