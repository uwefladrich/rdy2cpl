.PHONY: run clean realclean distclean _catch

_catch:
	@echo "Usage: make run|clean|realclean|distclean|ti"

work_files_ece = \
	work/ece-namcouple.yml \
	work/domain_cfg.nc

grid_files = \
	work/grids.nc \
	work/areas.nc \
	work/masks.nc

work:
	@mkdir -p $@

$(work_files_ece): work
	@cd work && ln -sf ../examples/$(notdir $@)

run: $(work_files_ece) realclean
	@cd work && \
	    mpirun -np 8 r2c ece-namcouple.yml

clean:
	@rm -f work/debug.*.* work/nout.0*

realclean: clean
	@rm -fr work/namcouple work/grids.nc work/areas.nc work/masks.nc work/rmp_*.nc

distclean:
	@rm -fr work

$(grid_files):
	$(error OASIS grid files missing! Make sure to run "make run" first)

ti-weights: $(work_files_ece) realclean
	@cd work && \
	    ln -sf ../examples/ti-namcouple.yml && \
	    mpirun -np 1 r2c ti-namcouple.yml

ti: $(grid_files)
	@cd work && \
	    ln -sf ../examples/ti-namcouple.yml && \
	    python ../utils/ti.py ti-namcouple.yml
