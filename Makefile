.PHONY: run clean realclean _catch

_catch:
	@echo "Usage: make run|clean|realclean"

run: realclean
	@${MPIRUN4PY} -np 11 python cli.py examples/ece-namcouple.yaml

clean:
	@rm -f debug.root.* debug.notroot.* nout.0*

realclean: clean
	@rm -fr namcouple grids.nc areas.nc masks.nc rmp_*.nc
