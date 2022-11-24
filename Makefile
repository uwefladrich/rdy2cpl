.PHONY: run clean realclean distclean _catch

_catch:
	@echo "Usage: make run|clean|realclean"

work_files_ece = \
	work/ece-namcouple.yml \
	work/domain_cfg.nc

work:
	@mkdir -p $@

$(work_files_ece): work
	@cd work && ln -sf ../examples/$(notdir $@)

run: $(work_files_ece) realclean
	@cd work && \
	    ${MPIRUN4PY} -np 8 r2c ece-namcouple.yml

clean:
	@rm -f work/debug.*.* work/nout.0*

realclean: clean
	@rm -fr work/namcouple work/grids.nc work/areas.nc work/masks.nc work/rmp_*.nc

distclean:
	@rm -fr work
