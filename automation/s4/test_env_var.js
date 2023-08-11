#!/usr/bin/env node

const my_variable = process.env["HEY"] != undefined ? process.env["HEY"] : "La variable no existe";
console.log(my_variable);
