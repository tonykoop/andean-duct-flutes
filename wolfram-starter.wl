(* Andean duct flute starter: open-pipe length and first-pass holes. *)

ClearAll["Global`*"];

cInPerSec = 13552;
a4 = 440;
fundamentalHz = 392.0;
boreIn = 0.625;
radiusIn = boreIn/2;
endCorrectionIn = 2*0.6*radiusIn;

targetHz[midi_] := a4*2^((midi - 69)/12);
centsError[measured_, target_] := 1200*Log[2, measured/target];
physicalLengthForHz[f_] := cInPerSec/(2*f) - endCorrectionIn;

scaleOffsets = {0, 3, 5, 7, 10, 12};
scaleTable = Table[
  With[{f = fundamentalHz*2^(offset/12)},
    <|
      "OffsetSemitones" -> offset,
      "TargetHz" -> f,
      "DistanceFromFootIn" -> physicalLengthForHz[fundamentalHz]*(fundamentalHz/f)
    |>
  ],
  {offset, scaleOffsets}
];

Dataset[scaleTable]

(* Validation reminder: duct/window response is empirical and must be measured
   before this model is used for a hardwood or bamboo body. *)
