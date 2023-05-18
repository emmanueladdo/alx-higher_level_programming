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

/**
 * print_python_bytes - Prints info about Python byte objects.
 * @p: A PyObject byte.
 */
void print_python_bytes(PyObject *p)
{
        unsigned char i, size;
        PyBytesObject *bytes = (PyBytesObject *)p;

        printf("[.] bytes object info\n");
        if (strcmp(p->ob_type->tp_name, "bytes") != 0)
        {
                printf("  [ERROR] Invalid Bytes Object\n");
                return;
        }

        printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
        printf("  trying string: %s\n", bytes->ob_sval);

        if (((PyVarObject *)p)->ob_size > 10)
                size = 10;
        else
                size = ((PyVarObject *)p)->ob_size + 1;

        printf("  first %d bytes: ", size);
        for (i = 0; i < size; i++)
        {
                printf("%02hhx", bytes->ob_sval[i]);
                if (i == (size - 1))
                        printf("\n");
                else
                        printf(" ");
        }
}
