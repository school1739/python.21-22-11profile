const path = require('path')
const fs = require('fs')
const express = require('express')
const app = express()
const port = 3000
const jszip = require('jszip')

/**
 * @param {string} path 
 */
function fileScanner(path) {
    let map = {}
    scan = (p) => {
        const paths = fs.readdirSync(p)
        for(let i = 0; i < paths.length; i++) {
            let e = paths[i]
            if(/\w+\.\w+/.test(e.split('/').pop()))  // If element is a file
                map[p] = e
            else {
                map[p] = e
                scan(`${p}/${e}`)
            }
        }
    }
    path.split('/').pop()
    scan(path)
    console.log(map)
}

app.get('/', (req, res) => {
    const baseDir = path.resolve(__dirname, '..', 'bundles', '1')

    fileScanner(baseDir)

    // res.sendFile('/Users/alexeytkachenko/Documents/PROJECTS/python.21-22-11profile/27/rep/1/1A.txt')
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port} `)
})

// http://10.161.16.235:3000/