#!/usr/bin/node
const [firstArg, secondArg] = process.argv.slice(2);

if (firstArg === undefined) {
  console.log("No argument");
} else {
  console.log(firstArg);
}
