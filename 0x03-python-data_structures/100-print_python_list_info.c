#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int siz, allo, i;
	PyObject *obj;

	siz = Py_SIZE(p);
	allo = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", siz);
	printf("[*] Allocated = %d\n", allo);

	for (i = 0; i < siz; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
