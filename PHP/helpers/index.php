<?php

require __DIR__ . '/vendor/autoload.php';

use App\Arr;

$array = [
    'foo' => 'bar',
    'baz' => ['bam' => 'foobar'],
    'eze' => 'soc'
];

$first = Arr::first($array);
echo $first . "\n"; // bar

$last = Arr::last($array);
echo $last . "\n"; // "soc"

$value = Arr::get('baz.bam', $array);
echo $value . "\n"; // "foobar"