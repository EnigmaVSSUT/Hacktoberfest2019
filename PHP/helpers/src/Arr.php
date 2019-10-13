<?php

namespace App;

class Arr
{
    /**
     * The value of the first element
     *
     * @param array $array
     * @return mixed
     */
    public static function first(array $array)
    {
        return $array[array_keys($array)[0]];
    }

    /**
     * The value of the last element
     *
     * @param array $array
     * @return mixed
     */
    public static function last(array $array)
    {
        return $array[array_keys($array)[sizeof($array) - 1]];
    }

    /**
     * The value of the specified key
     *
     * @param $key
     * @param array $array
     * @return mixed|null
     */
    public static function get($key, array $array)
    {
        if (is_string($key) && is_array($array)) {
            $keys = explode('.', $key);
            while (sizeof($keys) >= 1) {
                $k = array_shift($keys);
                if (!isset($array[$k])) {
                    return null;
                }
                if (sizeof($keys) === 0) {
                    return $array[$k];
                }
                $array = &$array[$k];
            }
        }
        return null;
    }
}
