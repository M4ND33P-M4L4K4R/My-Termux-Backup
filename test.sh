#if_elif_statement

echo -n "Enter A number : "
read Var


if [[ $Var -gt 10 ]]
then
	echo -e "\033[32mThe number is greater than 10."
elif [[ $Var -eq 10 ]] 
then 
	echo -e "\033[31mthis equal to 10"
else
	echo -e "\033[33mThe variableis less than 10"
fi
