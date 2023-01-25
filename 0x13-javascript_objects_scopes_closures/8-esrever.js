#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight((arr, current) => {
    arr.push(current);
    return arr;
  }, []);
};
