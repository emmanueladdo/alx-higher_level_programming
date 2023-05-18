#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about a Python list object
 * @p: Pointer to a PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about a Python bytes object
 * @p: Pointer to a PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t i;
	char *bytes = PyBytes_AsString(p);

	printf("[.] Bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes);

	if (size > 10)
	{
		size = 10;
	}

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02x", (unsigned char)bytes[i]);
		if (i < size - 1)
			printf(" ");
	}
	printf("\n");
}

