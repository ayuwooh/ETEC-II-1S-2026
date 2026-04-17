#!/bin/bash
                                                                                                                                            
nome=$1
square1=$2
square2=$3
tribase=$4
trialtura=$5
                                                                                                                                            
let sqresult=square1*square2
let triresult=(tribase*trialtura)/2
                                                                                                                                            
echo Boa Noite $nome
echo Área do quadrado: $sqresult ²
echo Área do triângulo: $triresult ²